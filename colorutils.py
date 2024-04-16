def add_list(list1, list2):
	# Check if the lists are of the same length
	if len(list1) != len(list2):
		raise "Lists must be of the same length to add them."

	# Use list comprehension to add corresponding elements
	result = [x + y for x, y in zip(list1, list2)]
	return result


def add_tuples(tuple1, tuple2):
	# Check if the tuples are of the same length
	if len(tuple1) != len(tuple2):
		raise "Tuples must be of the same length to add them."

	# Use tuple comprehension to add corresponding elements
	result = tuple(x + y for x, y in zip(tuple1, tuple2))
	return result


def subtract_list(list1, list2):
	# Check if the lists are of the same length
	if len(list1) != len(list2):
		raise "Lists must be of the same length to add them."

	# Use list comprehension to add corresponding elements
	result = [x - y for x, y in zip(list1, list2)]
	return result


def subtract_tuples(tuple1, tuple2):
	# Check if the tuples are of the same length
	if len(tuple1) != len(tuple2):
		raise "Tuples must be of the same length to add them."

	# Use tuple comprehension to add corresponding elements
	result = tuple(x - y for x, y in zip(tuple1, tuple2))
	return result


def scale_tuple(tuple_input, factor):
	scaled_tuple = tuple(x * factor for x in tuple_input)
	return scaled_tuple


def scale_list(list_input, factor):
	scaled_list = [x * factor for x in list_input]
	return scaled_list


def subtract_tuple(tuple_input, factor):
	scaled_tuple = tuple(x - factor for x in tuple_input)
	return scaled_tuple


def subtract_list(list_input, factor):
	scaled_list = [x - factor for x in list_input]
	return scaled_list


def multiply_tuples(t1, t2):
	return tuple(t1[x] * t2[x] for x in range(len(t1)))


def multiply_lists(*lists):
	if not lists:
		return []

	result = [x * y for x in lists[0] for y in zip(*lists[1:])]
	return result


def to_white(tpl, amount):
	tpl2 = scale_tuple(tuple(255 - x for x in tpl), amount)
	return tuple(255 - x for x in tpl2)


def round_tuple(tpl):
	return tuple([round(x) for x in tpl])
