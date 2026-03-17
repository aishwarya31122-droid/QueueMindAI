from geopy.distance import geodesic

class LocationAgent:

    def recommend_branch(self, user_location):

        branches = {
            "Branch A": (13.0827,80.2707),
            "Branch B": (13.0500,80.2120),
            "Branch C": (13.1200,80.3000)
        }

        wait_times = {
            "Branch A": 10,
            "Branch B": 6,
            "Branch C": 15
        }

        best_branch = None
        best_score = 999

        for name,coords in branches.items():

            distance = geodesic(user_location,coords).km

            score = distance + wait_times[name]

            if score < best_score:
                best_score = score
                best_branch = name

        return best_branch