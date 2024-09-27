class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def merge_sorted_lists(head1, head2):
  """
  Menggabungkan dua linked list yang diurutkan dan mengembalikan linked list gabungan yang diurutkan dari terkecil ke terbesar.

  Args:
    head1 (Node): Node awal dari linked list pertama.
    head2 (Node): Node awal dari linked list kedua.

  Returns:
    Node: Node awal dari linked list gabungan yang diurutkan.
  """
  # Inisialisasi node dummy untuk awal linked list gabungan
  dummy = Node(0)
  current = dummy

  # Menjelajahi kedua linked list secara bersamaan
  while head1 and head2:
    if head1.data <= head2.data:
      current.next = head1
      head1 = head1.next
    else:
      current.next = head2
      head2 = head2.next
    current = current.next

  # Menambahkan sisa node dari salah satu linked list ke linked list gabungan
  if head1:
    current.next = head1
  elif head2:
    current.next = head2

  # Mengembalikan node awal dari linked list gabungan
  return dummy.next

# Contoh penggunaan
# Input data linked list pertama
m = 5
head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)
head1.next.next.next = Node(7)

# Input data linked list kedua
n = 3
head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)

# Menggabungkan dan mengurutkan linked list
head_merged = merge_sorted_lists(head1, head2)

# Menampilkan isi linked list gabungan
current = head_merged
while current:
  print(current.data)
  current = current.next