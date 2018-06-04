import matplotlib.pyplot as plt
import numpy as np
import psutil
import time


def get_memory():
    return psutil.virtual_memory().percent


def get_cpu():
    return psutil.cpu_percent()


def get_stats():
    return get_memory(), get_cpu()


# init the figure components
fig, ax = plt.subplots()
ind = np.arange(1, 3)

# show the figure, but do not block
plt.show(block=False)

pm, pc = plt.bar(ind, get_stats())
pm.set_facecolor('r')
pc.set_facecolor('g')
ax.set_xticks(ind)
ax.set_xticklabels(['Memory', 'CPU'])
ax.set_ylim([0, 100])
ax.set_ylabel('Percent')
ax.set_title('System Monitor')


# flush the image display
def flush():
    fig.canvas.draw_idle()

    try:
        fig.canvas.flush_events()
    except NotImplementedError:
        pass
    fig.canvas.start_event_loop(1)


# update values
def update():
    m, c = get_stats()

    pm.set_height(m)
    pc.set_height(c)
    ax.texts = []  # clear texts before re-fill
    ax.text(1, m + 0.05, '%.0f' % m, ha='center', va='bottom', fontsize=15)
    ax.text(2, c + 0.05, '%.0f' % c, ha='center', va='bottom', fontsize=15)
    flush()
    print(time.asctime(time.localtime(time.time())) + '\tMem: %d\t\tCPU: %d' % (m, c))


while True:
    update()
