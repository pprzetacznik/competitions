from typing import Set, Dict
from dataclasses import dataclass, field
from unittest import TestCase, main


@dataclass(frozen=True)
class Package:
    name: str
    version: str
    dependencies_set: Set = field(hash=False)

    def __repr__(self) -> str:
        return f"{self.name}__{self.version}"


Conflicts = Dict[str, Dict[str, Package]]


def check_conflicts(package: Package, verbose: bool = False) -> Conflicts:
    visited_dict = {}
    flatten_packages = {}
    stack = [package]
    while stack:
        package = stack.pop()
        visited = visited_dict.get(package, False)
        if not visited:
            stack += list(package.dependencies_set)
            versions = flatten_packages.get(package.name, {})
            versions[package.version] = package
            flatten_packages[package.name] = versions
            visited_dict[package] = True
    result = {
        name: versions
        for name, versions in flatten_packages.items()
        if len(versions) > 1
    }
    if verbose:
        print(f"{visited_dict}")
        print(result)
    return result


class TestAdjMatrix(TestCase):
    def test_check_conflictss(self) -> None:
        package1 = Package("package1", "1.0", set([]))
        package1_conf = Package("package1", "2.0", set([]))
        package2 = Package("package2", "3.0", set([package1]))
        package3 = Package("package3", "4.0", set([package2]))
        package4 = Package(
            "package4", "5.0", set([package1_conf, package2, package3])
        )
        assert check_conflicts(package4, verbose=True)


if __name__ == "__main__":
    main()
