use std::{
    collections::{HashMap, VecDeque},
    num::ParseIntError,
    str::FromStr,
};

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum Material {
    Ore,
    Clay,
    Obsidian,
    Geode,
}

#[derive(Debug, Clone, Copy)]
struct Inventory {
    ore_robots: usize,
    clay_robots: usize,
    obsidian_robots: usize,
    geode_robots: usize,
    ores: usize,
    clay: usize,
    obsidian: usize,
    geodes: usize,
}

impl Inventory {
    fn new() -> Inventory {
        Inventory {
            ore_robots: 1,
            clay_robots: 0,
            obsidian_robots: 0,
            geode_robots: 0,
            ores: 0,
            clay: 0,
            obsidian: 0,
            geodes: 0,
        }
    }

    fn n_robots(&self, robot: Material) -> usize {
        match robot {
            Material::Ore => self.ore_robots,
            Material::Clay => self.clay_robots,
            Material::Obsidian => self.obsidian_robots,
            Material::Geode => self.geode_robots,
        }
    }

    fn unmine(self) -> Inventory {
        let mut other = self;
        other.ores -= other.ore_robots;
        other.clay -= other.clay_robots;
        other.obsidian -= other.obsidian_robots;
        other.geodes -= other.geode_robots;
        other
    }
    fn _mine(&mut self) {
        self.ores += self.ore_robots;
        self.clay += self.clay_robots;
        self.obsidian += self.obsidian_robots;
        self.geodes += self.geode_robots;
    }

    fn mine(self) -> Inventory {
        let mut other = self;
        other._mine();
        other
    }

    fn build(self, blueprint: &Blueprint, robot: Material) -> Inventory {
        let mut other = self;

        let RobotCost {
            ores,
            clay,
            obsidian,
        } = blueprint.cost(robot);

        other.ores -= ores;
        other.clay -= clay;
        other.obsidian -= obsidian;

        other._mine();

        match robot {
            Material::Ore => other.ore_robots += 1,
            Material::Clay => other.clay_robots += 1,
            Material::Obsidian => other.obsidian_robots += 1,
            Material::Geode => other.geode_robots += 1,
        };

        other
    }
}

#[derive(Debug, Clone, Copy)]
struct RobotCost {
    ores: usize,
    clay: usize,
    obsidian: usize,
}

#[derive(Debug)]
struct Blueprint {
    ore_robot: RobotCost,
    clay_robot: RobotCost,
    obsidian_robot: RobotCost,
    geode_robot: RobotCost,
}

impl FromStr for Blueprint {
    type Err = ParseIntError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let (_, rest) = s.split_once(':').unwrap();
        let mut segments = rest.trim().split_terminator('.');

        let ore_robot_cost: usize = segments
            .next()
            .unwrap()
            .trim()
            .trim_start_matches("Each ore robot costs ")
            .trim_end_matches(" ore")
            .parse()?;

        let clay_robot_cost: usize = segments
            .next()
            .unwrap()
            .trim()
            .trim_start_matches("Each clay robot costs ")
            .trim_end_matches(" ore")
            .parse()?;

        let (obsidian_robot_ore_cost, obsidian_robot_clay_cost): (usize, usize) = {
            let (ore, clay) = segments
                .next()
                .unwrap()
                .trim()
                .trim_start_matches("Each obsidian robot costs ")
                .trim_end_matches(" clay")
                .split_once(" ore and ")
                .unwrap();
            (ore.parse()?, clay.parse()?)
        };

        let (geode_robot_ore_cost, geode_robot_obsidian_cost): (usize, usize) = {
            let (ore, clay) = segments
                .next()
                .unwrap()
                .trim()
                .trim_start_matches("Each geode robot costs ")
                .trim_end_matches(" obsidian")
                .split_once(" ore and ")
                .unwrap();
            (ore.parse()?, clay.parse()?)
        };

        Ok(Blueprint {
            ore_robot: RobotCost {
                ores: ore_robot_cost,
                clay: 0,
                obsidian: 0,
            },
            clay_robot: RobotCost {
                ores: clay_robot_cost,
                clay: 0,
                obsidian: 0,
            },
            obsidian_robot: RobotCost {
                ores: obsidian_robot_ore_cost,
                clay: obsidian_robot_clay_cost,
                obsidian: 0,
            },
            geode_robot: RobotCost {
                ores: geode_robot_ore_cost,
                clay: 0,
                obsidian: geode_robot_obsidian_cost,
            },
        })
    }
}

impl Blueprint {
    fn cost(&self, robot: Material) -> RobotCost {
        match robot {
            Material::Ore => self.ore_robot,
            Material::Clay => self.clay_robot,
            Material::Obsidian => self.obsidian_robot,
            Material::Geode => self.geode_robot,
        }
    }

    fn can_build(&self, inv: &Inventory, robot: Material) -> bool {
        let RobotCost {
            ores,
            clay,
            obsidian,
        } = self.cost(robot);

        inv.ores >= ores && inv.clay >= clay && inv.obsidian >= obsidian
    }

    /// More than just "can we build", but should we?
    /// Returns false if we already produce 1 robots worth of this material per minute
    /// or if we skipped building this robot before this turn
    fn should_build(&self, inv: &Inventory, robot: Material, built: bool) -> bool {
        if robot == Material::Geode {
            return true;
        };

        let material_cost = |c: RobotCost| match robot {
            Material::Ore => c.ores,
            Material::Clay => c.clay,
            Material::Obsidian => c.obsidian,
            Material::Geode => unreachable!(),
        };

        let max_cost = [
            self.ore_robot,
            self.clay_robot,
            self.obsidian_robot,
            self.geode_robot,
        ]
        .into_iter()
        .map(material_cost)
        .max()
        .unwrap_or(0);

        let still_needed = inv.n_robots(robot) < max_cost;

        if !built {
            let prev_inventory = inv.unmine();
            let skipped = self.can_build(&prev_inventory, robot);
            still_needed && !skipped
        } else {
            still_needed
        }
    }
}

fn search(factory: &Blueprint, minutes: i32) -> usize {
    // BFS queue
    let mut queue = VecDeque::new();
    queue.push_back((Inventory::new(), 0, false));

    // store best geode score at each time
    let mut cache: HashMap<i32, usize> = HashMap::new();
    for i in 0..=minutes {
        cache.insert(i, 0);
    }

    while let Some((inv, min, built)) = queue.pop_front() {
        let &prior_best = cache.get(&min).unwrap();

        // dead end - we already have a faster route
        if inv.geodes < prior_best {
            continue;
        }
        cache.insert(min, prior_best.max(inv.geodes));

        // we're done
        if min == minutes {
            continue;
        }

        // greedy - build a geode whenever you can, don't expore other options
        if factory.can_build(&inv, Material::Geode) {
            queue.push_back((inv.build(factory, Material::Geode), min + 1, true));
            continue;
        }

        queue.push_back((inv.mine(), min + 1, false));

        for robot in [Material::Obsidian, Material::Clay, Material::Ore] {
            // assuming we can only build 1 robot at a time
            if factory.can_build(&inv, robot) && factory.should_build(&inv, robot, built) {
                queue.push_back((inv.build(factory, robot), min + 1, true));
            }
        }
    }

    *cache.get(&minutes).unwrap()
}

fn solve_part_1(blueprints: &[Blueprint]) -> usize {
    blueprints
        .iter()
        .enumerate()
        .map(|(i, blueprint)| {
            let geode_score = search(blueprint, 24);
            geode_score * (i + 1)
        })
        .sum()
}

fn solve_part_2(blueprints: &[Blueprint]) -> usize {
    blueprints
        .iter()
        .take(3)
        .map(|blueprint| search(blueprint, 32))
        .product()
}

fn solve_day_19(input: &str) -> (usize, usize) {
    let blueprints: Vec<Blueprint> = input.lines().map(|s| s.parse().unwrap()).collect();

    (solve_part_1(&blueprints), solve_part_2(&blueprints))
}
fn main() {
    let input = include_str!("day19input.txt");

    let (part_1, part_2) = solve_day_19(input);

    println!("Quality Levels: {}", part_1);

    println!("Max geode product: {}", part_2);
}

#[cfg(test)]
const EXAMPLE_DATA: &str = include_str!("day19input.txt");

#[test]
fn example() {
    let (part_1, part_2) = solve_day_19(EXAMPLE_DATA);
    assert_eq!(part_1, 33);
    assert_eq!(part_2, 3472);
}
