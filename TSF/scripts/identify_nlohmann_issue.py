import sys

def comment_nlohmann_misbehaviours(id: int) -> None:
    with open("./TSF/docs/nlohmann_misbehaviours_comments.md") as f:        
        for line in f:
            # look for the issue id
            cols = line.split("|")
            if cols[0].strip() == str(id) and len(cols)>1:
                # read the candidate comment
                candidate = cols[1].strip()
                # if there is something to comment, do it
                if candidate != "":
                    print(f"- **Comment:** {candidate}")
                # each issue can only have one comment listed
                return
    # if there is no comment to be found, nothing is done


if __name__ == "__main__" and len(sys.argv)>1:
    # split input into what is assumed to be the numbers of the issues.
    inputs = sys.argv[1:]
    # try to parse inputs into integer
    try:
        numerical_inputs = [int(i) for i in inputs]
    except ValueError:
        raise RuntimeError("Only integer numbers are accepted to identify issues.")
    
    list(map(comment_nlohmann_misbehaviours,numerical_inputs))
