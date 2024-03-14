
import statistics

#list = [0, 0, 1, 1]
list = [1, 2, 3, 4,5]
print("List : " + str(list))

st_dev = statistics.pstdev(list)
print("Standard deviation of the given list: " + str(st_dev))
print("Media : " + str(statistics.mean(list)))