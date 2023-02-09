from stats.datacapture import DataCapture


if __name__ == '__main__':
    capture = DataCapture()
    capture.add(0)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    print(stats.between(4, 9))
