import argparse
import re
import requests
import hashlib
from pathlib import Path

def main() -> None:
    ap = argparse.ArgumentParser(description="little helper script automatically updating version numbers and release dates")
    ap.add_argument("-v",
                    "--version", 
                    help="version number to be updated to; if unspecified, most recent version is chosen",
                    default=None
                    )
    ap.add_argument("-c",
                    "--check",
                    help="checks whether current and specified (or most recent) version of single_include/nlohmann/json.hpp coincide; no other action is performed",
                    action=argparse.BooleanOptionalAction
                    )
    ap.add_argument("-a",
                    "--auto",
                    help="automatically updates all options",
                    action=argparse.BooleanOptionalAction
                    )
    ap.add_argument("-u",
                    "--update",
                    action='append',
                    choices=["JLS-01","JLS-06","JLS-07","JLS-11","JLS-14","introduction","misbehaviours"],
                    help="updates the specified file(s):" \
                            " JLS-01 - TSF/trustable/JLS-01.md," \
                            " JLS-06 - TSF/trustable/JLS-06.md," \
                            " JLS-07 - TSF/trustable/JLS-07.md," \
                            " JLS-11 - TSF/trustable/JLS-11.md," \
                            " JLS-14 - TSF/trustable/JLS-14.md," \
                            " introduction - TSF/docs/introduction/index.rst," \
                            " misbehaviours - TSF/scripts/generate_list_of_misbehaviours.py",
                    default=None
                    )
    ap.add_argument("-b",
                    "--branch",
                    help="name of the branch to which the references for branch protection and workflow-failures point to",
                    default=None
                    )
    ap.add_argument("-bo",
                    "--branch_only",
                    help="adapts branch-names only",
                    action=argparse.BooleanOptionalAction
                    )
    args = ap.parse_args()

    root = Path(__file__).resolve().parent.parent.parent

    print(args)

    if (not args.check
        and (
            (not args.auto
             and args.update is None)
            or (args.branch_only
                and args.branch is None)
            )
        ):
        # do nothing    
        return None

    # Fetch the metadata
    version, url, release_date, expected_sha = fetch_metadata(args.version)

    # if flag check is set, then the sha of single_include/nlohmann/json.hpp is cross-checked with the sha of the specified version 
    if args.check:
        if not check(expected_sha,root):
            if args.version is None:
                print(f"The current version of single_include/nlohmann/json.hpp is not the most recent one, which is {version}.")
            else:
                print(f"The current version of single_include/nlohmann/json.hpp does not coincide with {version}.")
        else:
            if args.version is None:
                print(f"The current version of single_include/nlohmann/json.hpp is the most recent one, which is {version}.")
            else:
                print(f"The current version of single_include/nlohmann/json.hpp coincides with {version}.")
        # No other action is performed.
        return None
    if not check(expected_sha,root):
        print("\nWARNING! The current version of single_include/nlohmann/json.hpp does not coincide with {version}.\n\nIf you proceed, then the documentation is expected to contain wrong data!")
        user = input("Proceed anyway? [y/n] ").strip().lower()
        if user != "y":
            print("Aborting update ...")
            return None
    # if flag auto is set, then all is updated automatically
    if args.auto:
        if args.branch is not None:
            update_JLS_01(args.branch,root)
            update_JLS_06(args.branch,root)
            update_JLS_07(args.branch,root)
        if not args.branch_only:
            update_JLS_11(release_date,root)
            update_JLS_14(url,expected_sha,root)
            update_intro(version,root)
            update_misbehaviours(version,release_date,root)
        # no other action is necessary
        return None
    if "JLS-01" in args.update:
        update_JLS_01(args.branch,root)
    if "JLS-06" in args.update:
        update_JLS_06(args.branch,root)
    if "JLS-07" in args.update:
        update_JLS_07(args.branch,root)
    if args.branch_only:
        return None
    if "JLS-11" in args.update:
        update_JLS_11(release_date,root)
    if "JLS-14" in args.update:
        update_JLS_14(url,expected_sha,root)
    if "introduction" in args.update:
        update_intro(version,root)
    if "misbehaviours" in args.update:
        update_misbehaviours(version,release_date,root)

def update_JLS_01(branch: str, root: Path | None = None) -> None:
    if root is None:
        root = Path(__file__).resolve().parent.parent
        path_to_jls_11 = root / "trustable/statements/JLS-01.md"
    else:
        path_to_jls_11 = root / "TSF/trustable/statements/JLS-01.md"
    data = path_to_jls_11.read_text(encoding='utf-8')
    data = re.sub(r'(?m)^(\s*branch:\s*")([^"]*)(")', r'\g<1>' + branch + r'\g<3>', data)
    path_to_jls_11.write_text(data)

def update_JLS_06(branch: str, root: Path | None = None) -> None:
    if root is None:
        root = Path(__file__).resolve().parent.parent
        path_to_jls_11 = root / "trustable/statements/JLS-06.md"
    else:
        path_to_jls_11 = root / "TSF/trustable/statements/JLS-06.md"
    data = path_to_jls_11.read_text(encoding='utf-8')
    data = re.sub(r'(?m)^(\s*branch:\s*")([^"]*)(")', r'\g<1>' + branch + r'\g<3>', data)
    path_to_jls_11.write_text(data)

def update_JLS_07(branch: str, root: Path | None = None) -> None:
    if root is None:
        root = Path(__file__).resolve().parent.parent
        path_to_jls_11 = root / "trustable/statements/JLS-07.md"
    else:
        path_to_jls_11 = root / "TSF/trustable/statements/JLS-07.md"
    data = path_to_jls_11.read_text(encoding='utf-8')
    data = re.sub(r'(?m)^(\s*branch:\s*")([^"]*)(")', r'\g<1>' + branch + r'\g<3>', data)
    path_to_jls_11.write_text(data)

def update_JLS_11(release_date: str, root: Path | None = None) -> None:
    if root is None:
        root = Path(__file__).resolve().parent.parent
        path_to_jls_11 = root / "trustable/statements/JLS-11.md"
    else:
        path_to_jls_11 = root / "TSF/trustable/statements/JLS-11.md"
    data = path_to_jls_11.read_text(encoding='utf-8')
    data = re.sub(r'(?m)^(\s*release_date:\s*")([^"]*)(")', r'\g<1>' + release_date + r'\g<3>', data)
    path_to_jls_11.write_text(data)

def update_JLS_14(url: str, sha: str, root: Path | None = None) -> None:
    if root is None:
        root = Path(__file__).resolve().parent.parent
        path_to_jls_14 = root / "trustable/statements/JLS-14.md"
    else:
        path_to_jls_14 = root / "TSF/trustable/statements/JLS-14.md"
    data = path_to_jls_14.read_text(encoding='utf-8')
    data = re.sub(r'(?m)^(\s*sha:\s*")([^"]*)(")', r'\g<1>' + sha + r'\g<3>', data)
    data = re.sub(r'(?m)^(\s*url:\s*")([^"]*)(")', r'\g<1>' + url + r'\g<3>', data)
    path_to_jls_14.write_text(data)

def update_intro(version: str, root: Path | None = None) -> None:
    if root is None:
        root = Path(__file__).resolve().parent.parent
        path_to_intro = root / "docs/introduction/index.rst"
    else:
        path_to_intro = root / "TSF/docs/introduction/index.rst"
    data = path_to_intro.read_text(encoding='utf-8')
    data = re.sub(r'(\(version\s+)([^)]*)(\))',
              lambda m: f"{m.group(1)}{version}{m.group(3)}",
              data)
    path_to_intro.write_text(data)

def update_misbehaviours(version: str, release_date: str, root: Path | None = None) -> None:
    if root is None:
        root = Path(__file__).resolve().parent
        path_to_script = root / "generate_list_of_misbehaviours.py"
    else:
        path_to_script = root / "TSF/scripts/generate_list_of_misbehaviours.py"
    data = path_to_script.read_text(encoding='utf-8')
    data = re.sub(r'(?m)^(\s*version\s*=\s*")([^"]*)(")', r'\g<1>' + version + r'\g<3>', data)
    data = re.sub(r'(?m)^(\s*release_date\s*=\s*")([^"]*)(")', r'\g<1>' + release_date + r'\g<3>', data)
    path_to_script.write_text(data)


def fetch_metadata(version = None) -> tuple[str,str,str]:
    # This function fetches the metadata of the release of the version of nlohmann/json specified in the input.
    # If the input is None, then the most recent version is fetched.
    # The function returns the version number, the release date in the format %Y-%m-%dT%H:%M:%SZ 
    # and the sha256-value of the json.hpp of the released version

    if version is None:
        version = ""

    # fetch the sha-value of most recent release
    releases = requests.get("https://github.com/nlohmann/json/releases")
    if releases.status_code != 200:
        raise Warning("The release page of nlohmann/json appears to be currently not reachable.")
    releases_by_the_line = releases.text.splitlines()
    # releases is expected to be huge, delete to free up room
    del releases
    found_version = False
    found_sha = False
    found_release_date = False
    found_tag = False
    for line in releases_by_the_line:
        # look for 
        if not found_version and f"JSON for Modern C++ version {version}" not in line:
            continue
        elif not found_version:
            if version == "":
                m = re.search(r'JSON for Modern C\+\+ version\s*([^<"]*)<',line)
                if m is None:
                    raise RuntimeError("Critical Error: Can not find version number of most recent release!")
                version = m.group(1)
            found_version = True
            continue
        if not found_release_date and "datetime=" in line:
            m = re.search(r'datetime\s*=\s*"([^"]*)"', line)
            if m is None:
                raise RuntimeError(f"Critical Error: Can not find release-date of version {version}!")
            release_date = m.group(1) if m else None
            found_release_date = True
        if not found_sha and "SHA-256:" in line and "(json.hpp)" in line:
            expected_sha = line.split("SHA-256:", 1)[1].split("(json.hpp)", 1)[0].strip()
            found_sha = True
        if not found_tag and "/nlohmann/json/tree" in line:
            m = re.search(r'href\s*=\s*"([^"]*)"', line)
            if m is None:
                raise RuntimeError(f"Critical Error: Can not find link to release version {version}!")
            url = "https://github.com" + m.group(1)
            found_tag = True
        if found_version and found_sha and found_release_date and found_tag:
            return (version, url, release_date, expected_sha)
        if "JSON for Modern C++ version" in line and f"JSON for Modern C++ version {version}" not in line:
            if not found_version and not found_release_date and not found_tag:
                error_message = "Could not find any metadata"
            elif not found_sha:
                error_message = "Could not find SHA-value for json.hpp"
                if not found_release_date:
                    error_message += " and relase-date"
                elif not found_tag:
                    error_message += " and link to code"
            elif not found_release_date:
                error_message = "Could not find release-date"
                if not found_tag:
                    error_message += " and link to code"
            else:
                error_message = "Could not find link to code"
            error_message += f" of version {version}!" if version!="" else " of most recent version!"
            raise RuntimeError(error_message)
    # If ever the for-loop comes to its end, the specified version can not be found!
    raise RuntimeError(f"Can not locate the release of version {version}!")


def check(expected_sha: str, root: Path | None = None) -> bool:
    # get the actual sha-value of the single_include.json
    if root is None:
        root = Path(__file__).resolve().parent.parent.parent
    single_include_json_path = root / "single_include/nlohmann/json.hpp" 
    with single_include_json_path.open('rb') as f:
        actual_sha = hashlib.file_digest(f, 'sha256').hexdigest()
    return actual_sha == expected_sha


if __name__ == "__main__":
    main()