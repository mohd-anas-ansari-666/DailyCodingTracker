import requests

def get_leetcode_stats(username):
    query = """
    query getUserProfile($username: String!) {
      matchedUser(username: $username) {
        submitStatsGlobal {
          acSubmissionNum {
            difficulty
            count
          }
        }
      }
    }
    """

    r = requests.post(
        "https://leetcode.com/graphql",
        json={"query": query, "variables": {"username": username}}
    )

    data = r.json()
    stats = data["data"]["matchedUser"]["submitStatsGlobal"]["acSubmissionNum"]
    return sum([x["count"] for x in stats])
