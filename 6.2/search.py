file = open("6.2/spotify.csv", encoding="utf-8")
junk = file.readline()

drake_data = []

for line in file:
	items = line.strip().split(",")
	artist = str(items[-1])
	songtitle = str(items[-2])
	danceability = float(items[1])
	
	if artist == "Drake":
		drake_data.append([danceability, songtitle, artist])

print("Dance score \tSong")
for item in drake_data:
	print(str(item[0]) + "\t\t" + item[1] + " by " + item[2])

for i in range(len(drake_data)):
	currentMinimum = drake_data[i]
	smallest_index = i

	for j in range(i+1, len(drake_data)):
		if drake_data[j] < currentMinimum:
			currentMinimum = drake_data[j]
			smallest_index = j
	
	drake_data[smallest_index], drake_data[i] = drake_data[i], drake_data[smallest_index]

print(drake_data)