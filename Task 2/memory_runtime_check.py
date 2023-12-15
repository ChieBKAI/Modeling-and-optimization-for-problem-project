import networkx as nx
import random
import time
from memory_profiler import profile
random.seed(1)

@profile
def model(G):
    flow_cost, flow_dict = nx.capacity_scaling(G, demand='demand', capacity='capacity', weight='weight')
    return flow_cost, flow_dict

if __name__ == "__main__":
    for num_node in range(3, 50, 1):
        grid_size = num_node  # Kích thước lưới
        rows = grid_size + 1 
        cols = grid_size + 1
        G = nx.DiGraph()

        positions = {}  # Dictionary lưu trữ vị trí của các nodes

        # Thêm source
        G.add_node('source', demand=0, pos=(0, 0))
        positions['source'] = (0, 0)

        # Thêm các cạnh theo hướng từ trái sang phải và từ trên xuống dưới
        for i in range(1, rows):
            for j in range(1, cols):
                # Thêm node vào đồ thị
                G.add_node((i, j), demand=0, pos=(i, j))
                positions[(i, j)] = (i, j)

                # Thêm cạnh đi xuống (dưới) nếu không phải là hàng cuối cùng
                if i < rows - 1:
                    G.add_edge((i, j), (i + 1, j), weight=random.randint(1, 30), capacity=random.randint(7*grid_size, 10*grid_size))

                # Thêm cạnh đi qua phải nếu không phải là cột cuối cùng
                if j < cols - 1:
                    G.add_edge((i, j), (i, j + 1), weight=random.randint(1, 30), capacity=random.randint(7*grid_size, 10*grid_size))

        # Thêm sink
        G.add_node('sink', demand=0, pos=(rows, cols))
        positions['sink'] = (rows, cols)

        # Thêm cạnh đi từ source đến hàng đầu tiên và từ hàng cuối cùng đến sink
        for i in range(1, rows):
            G.add_edge('source', (i, 1), weight=0, capacity=9999)
            G.add_edge((i, cols - 1), 'sink', weight=0, capacity=9999)

        # Thêm demand cho source và sink
        G.nodes['source']['demand'] = -15 * grid_size
        G.nodes['sink']['demand'] = 15 * grid_size

        # Tính thời gian chạy thuật toán
        start_time = time.time()
        flow_cost, flow_dict = model(G)
        end_time = time.time()
        print(end_time - start_time)