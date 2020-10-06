import sys


POSITIONS = {
	15612504, # Oct 1, 0xEE3A58
	15631032  # Aug 5, 0xEE82B8
}
sup = True

with open(sys.argv[1], 'rb+') as f:
	for pos in POSITIONS:
		f.seek(pos)
		current = f.read(3)
		if current == b'\x45\x31\xc0':
			print("Already patched.")
			break
		elif current == b'\x44\x8b\xc5':
			f.seek(pos)
			f.write(b'\x45\x31\xc0')
			print("OK.")
			sup = True
			break
		else:
			sup = False

if not sup:
	print("Unsupported exe.")
input("Press enter to exit.")
