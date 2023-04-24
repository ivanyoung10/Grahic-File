packet_input = ["S Mary", "P Dee", "P Dee", "E Eileen", "E Mike", "E Joe", "P Dee",
                "E Vicky", "E George", "P Dee", "P Joe", "E Sally", " P Joe", "S Pete",
                "P Dee", "S Bill", "S Chase", "E Price",
                "P Dee", "E Sue"]

packet_input_length = len(packet_input)

p_queue = []
s_queue = []
e_queue = []

for x in range(packet_input_length):
    packet_in = packet_input[x]
    pclass = packet_in[0]
    if "P" == pclass:
        p_queue.append(packet_input[x])
    elif "S" == pclass:
        s_queue.append(packet_input[x])
    if "E" == pclass:
        e_queue.append(packet_input[x])
y = 0
while y < 8:
    for p in range(3):
        try:
            print(p_queue.pop(0))
        except:
            break

    for s in range(2):
        try:
            print(s_queue.pop(0))
        except:
            break
    for e in range(1):
        try:
            print(e_queue.pop(0))
        except:
            break

    y = y + 1
