import requests

def get_leetcode_difficulty_stats(username):
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
    ).json()

    stats = r["data"]["matchedUser"]["submitStatsGlobal"]["acSubmissionNum"]

    # Stats come as list of {difficulty: easy/medium/hard, count: N}
    result = {"Easy": 0, "Medium": 0, "Hard": 0}
    for item in stats:
        diff = item["difficulty"]
        result[diff] = item["count"]

    return result
