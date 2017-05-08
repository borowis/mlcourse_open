import sys

etalon_tags = ["javascript", "java", "python", "ruby", "php", "c++", "c#", "go", "scala", "swift"]
etalon_tags_set = set(etalon_tags)

input_f  = sys.argv[1]
output_f = sys.argv[2]

f_out = open(output_f, 'w')
with open(input_f) as f:
	for line in f:
		splitted = line.split("\t")
		if len(splitted) != 2:
			continue
	
		tags = set(splitted[1].strip().split(" ")) - set([''])
		intersect = list(tags & etalon_tags_set)
		if len(intersect) != 1:
			continue

		processed_label = etalon_tags.index(intersect[0]) + 1
		processed_text = splitted[0].strip().replace(":", "").replace("|", "")

		if len(processed_text) < 1:
			continue

		f_out.write(str(processed_label) + ' | ' + processed_text + '\n')

f_out.close()
