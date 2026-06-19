class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = defaultdict(list)
        email_to_name = {}
        
        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                adj[first_email].append(email)
                adj[email].append(first_email)
                email_to_name[email] = name
        visited = set()
        res = []
        def dfs(email,component):
            visited.add(email)
            component.append(email)
            for neighbor in adj[email]:
                if neighbor not in visited:
                    dfs(neighbor, component)
        for email in email_to_name:
            if email not in visited:
                component = []
                dfs(email,component)

                res.append([email_to_name[email]] + sorted(component))
        return res