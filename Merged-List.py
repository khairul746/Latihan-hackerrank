head1 = [1, 4, 5, 8]
head2 = [2, 3, 6, 7]

# Fungsi untuk menggabungkan dua linked list yang telah diurutkan
def merge_lists(head1, head2):
    merged_list = []
    i = j = 0

    # Lakukan penggabungan sampai salah satu linked list habis
    while i < len(head1) and j < len(head2):
        if head1[i] <= head2[j]:
            merged_list.append(head1[i])
            i += 1
        else:
            merged_list.append(head2[j])
            j += 1

    # Tambahkan sisa elemen dari linked list yang belum habis
    merged_list.extend(head1[i:])
    merged_list.extend(head2[j:])

    return merged_list

# Panggil fungsi untuk menggabungkan linked list
result = merge_lists(head1, head2)
print(result)