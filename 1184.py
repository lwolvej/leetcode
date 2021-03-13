class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        d, rd, n, now = 0, 0, len(distance), start
        while now != destination:
            d += distance[now]
            now = (now + 1) % n
        now = start
        while now != destination:
            now = (now - 1) % n
            rd += distance[now]
        return min(rd, d)


if __name__ == '__main__':
    print(-1 % 10)
