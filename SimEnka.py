import sys
import numpy as np

sim_raw = input("")
states_raw = input("")
symbols_raw = input("")
acc_states_raw = input("")
init_state = input("")

sim_arr = []
el_arr = sim_raw.split("|")
for el in el_arr:
    sim_arr.append(el.split(","))

states_arr = np.array(states_raw.split(","))
symbols_arr = np.array(symbols_raw.split(","))
symbols_arr = np.insert(symbols_arr, 0, '$', axis=0)
acc_states_arr = np.array(acc_states_raw.split(","))

nka_arr = np.full([states_arr.size, states_arr.size], fill_value=-1)

for line in sys.stdin:
    temp = line[:-1].split("->")
    current_state = temp[0].split(",")[0]
    delta = temp[0].split(",")[1]
    next_states = temp[1].split(",")
    if np.isin("#", next_states):
        continue
    current_state_id = np.searchsorted(states_arr, current_state)
    for el in np.searchsorted(states_arr, next_states):
        nka_arr[current_state_id][el] = np.searchsorted(symbols_arr, delta)

print(nka_arr)