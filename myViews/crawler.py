import requests
from bs4 import BeautifulSoup
from collections import deque

def dfs_crawler(seed_url, max_pages=10):
    visited = set()
    stack = [(seed_url, 0)]
    result = []

    while stack and len(visited) < max_pages:
        url, depth = stack.pop()

        if url in visited:
            continue

        visited.add(url)
        result.append(url)

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            for link in soup.find_all('a', href=True):
                next_url = link['href']
                if next_url.startswith('http') and next_url not in visited:
                    stack.append((next_url, depth + 1))
        except Exception as e:
            print(f"Error: {e}")

    return result

def bfs_crawler(seed_url, max_pages=10):
    visited = set()
    queue = deque([(seed_url, 0)])
    result = []

    while queue and len(visited) < max_pages:
        url, depth = queue.popleft()

        if url in visited:
            continue

        visited.add(url)
        result.append(url)

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            for link in soup.find_all('a', href=True):
                next_url = link['href']
                if next_url.startswith('http') and next_url not in visited:
                    queue.append((next_url, depth + 1))
        except Exception as e:
            print(f"Error: {e}")

    return result

# Example usage
seed_url = 'https://example.com'
max_pages = 5

print("DFS Crawler:")
dfs_result = dfs_crawler(seed_url, max_pages)
print(dfs_result)

print("\nBFS Crawler:")
bfs_result = bfs_crawler(seed_url, max_pages)
print(bfs_result)
