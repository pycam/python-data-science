from Bio import SeqIO
from Bio.SeqUtils import GC

# Read in a FASTA file named data/sample.fa
seq_records = list(SeqIO.parse('data/sample.fa', 'fasta'))

# find the number of sequences present in the file
num_seq = len(seq_records)
print('Total number of sequences:', num_seq)

# find IDs and lengths of the longest and the shortest sequences
max_len = min_len = len(seq_records[0].seq)

longest_seq = shortest_seq = seq_records[0].id

for i in range(1, num_seq):
    if len(seq_records[i].seq) > max_len:
        # update max_len and longest_seq
        max_len = len(seq_records[i].seq)
        longest_seq = seq_records[i].id
    elif len(seq_records[i].seq) < min_len:
        # update min_len and shortest_seq
        min_len = len(seq_records[i].seq)
        shortest_seq = seq_records[i].id

print('Longest sequence is', longest_seq, 'with length', max_len, 'bp')
print('Shortest sequence is', shortest_seq, 'with length', min_len, 'bp')

# Creating a new sequence list containing sequences longer than 500bp
# Calculate the average length of these sequences
# calculate and print the percentage of GC contents

long_seq_records = list()  # empty list for sequences

total_seq_length = 0
for sequence in seq_records:
    if len(sequence) > 500:
        long_seq_records.append(sequence)
        total_seq_length += len(sequence)
        gc = GC(sequence.seq)
        print('%GC in', sequence.id, 'is {:.2f}'.format(gc))

avg_seq_length = total_seq_length / len(long_seq_records)

print('Average length for sequences longer than 500bp is', avg_seq_length)

# Write sequences in the long_seq_records in a file with 'GenBank' format
SeqIO.write(long_seq_records, 'long_sequences.fa', 'fasta')
