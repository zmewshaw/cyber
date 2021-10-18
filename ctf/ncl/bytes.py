# def verify(submission):
#     processed = [ ]
#     if len(submission) % 2 != 0:    # Input is even
#         return False

#     for i in range(0, len(submission) / 2): # In range of half submission
#         processed.append(int(submission[i * 2] + submission[(i * 2) + 1], 16))  # Append integers (@ i*2 + @ (I*2)+1) make them base 16

#     ekc = [ 0x53, 75, 0x59, 0x2D, 0110, 0x45, 88, 65, 0x2D, 0x36, 0x35, 0x33, 0x38 ]
#     if len(processed) != len(ekc):  # Make sure len(processed) = 13 SUBMISSION IS A STRING OF 26 NUMBERS
#         return False

#     for i in range(len(processed)): # PROCESSED MUST BE EQUAL TO EKC
#         if ekc[i] != processed[i]:
#             return False

#     return True
input = ""
print(int(input[0], 16))