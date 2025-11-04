import json
from datetime import datetime, timezone
from identify_nlohmann_issue import comment_nlohmann_misbehaviours

version = "3.12.0"
release_date = "2025-04-11T08:43:39Z"

if __name__ == "__main__":
    release_time = datetime.strptime(release_date,"%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp()

    # fetch relevant issues
    with open("raw_open_issues.json") as list_1:
        all_open_issues = json.load(list_1)
    relevant_open_issues = [all_open_issues[i] for i in range(0,len(all_open_issues))
                                if len(all_open_issues[i].get("labels",[]))!=0 
                                and (all_open_issues[i].get("labels"))[0].get("name") == "kind: bug"
                            ]
    with open("raw_closed_issues.json") as list_2:
        all_closed_issues = json.load(list_2)
    relevant_closed_issues = [all_closed_issues[i] for i in range(0,len(all_closed_issues))
                                    if len(all_closed_issues[i].get("labels",[]))!=0 
                                    and (all_closed_issues[i].get("labels"))[0].get("name") == "kind: bug"
                                    and datetime.strptime(all_closed_issues[i].get("createdAt","2000-01-01T00:00:00Z"),"%Y-%m-%dT%H:%M:%SZ")
                                                                                .replace(tzinfo=timezone.utc)
                                                                                .timestamp()
                                        >=release_time
                            ]
    
    print("# Misbehaviours Report\n")
    print(f"This report lists known misbehaviours or bugs of version {version} of the nlohmann/json repository.")
    print("The misbehaviours are compiled from github issues of the nlohmann/json repository, and link to each corresponding issue.\n")


    print("## Open issues\n")
    for issue in relevant_open_issues:
        print(f'### [#{issue.get("number")}]({issue.get("url")})\n- **Title:** {issue.get("title")}\n- **State:** {issue.get("state")}\n- **Created At:** {issue.get("createdAt")}\n')
        comment_nlohmann_misbehaviours(int(issue.get("number")))
        print("\n")

    print(f"\n## Closed Issues (since version {version}\n")    
    for issue in relevant_closed_issues:
        print(f'### [#{issue.get("number")}]({issue.get("url")})\n- **Title:** {issue.get("title")}\n- **State:** {issue.get("state")}\n- **Created At:** {issue.get("createdAt")}\n')
        comment_nlohmann_misbehaviours(int(issue.get("number")))
        print("\n")
        
