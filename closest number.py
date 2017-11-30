m = int(input())
br = input().split()
br = sorted(list(map(int, br)))
initial_diff = br[1] - br[0]
final = str(br[0]) + ' ' + str(br[1]) + ' '
for i in range(2, len(br)):
    diff = (br[i] - br[i - 1])
    if (diff < initial_diff):
        final = ''
        final = str(br[i - 1]) + ' ' + str(br[i]) + ' '
        initial_diff = diff
    elif (diff == initial_diff):
        final = final + str(br[i - 1]) + ' ' + str(br[i]) + ' '

print(final)