class algorithm:
    def check(self, arr):
        res = 0

        for i in range(0,12):
            if (i % 2) == 0:
                res += arr[i]
            else:
                res += 3 * arr[i]

        if arr[12] == (10- (res % 10)):
            return True
        else:
            return False

    def find(self, arr):
        res = 0

        for i in range(0,12):
            if (i % 2) == 0:
                res += arr[i]
            else:
                res += 3 * arr[i]

        return 10- (res % 10)
