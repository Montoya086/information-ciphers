echo "------ Running Caesar Cipher ------"
echo "CIPHER"
python3 caesar.py -c << EOF
hello world
EOF
echo ""
echo "DECIPHER"
python3 caesar.py -d << EOF
khññr zruñg
EOF

echo "------ Running afin Cipher ------"
echo "CIPHER"
python3 afin.py -c << EOF
4
8
atacar al amanecer
EOF
echo ""
echo "DECIPHER"
python3 afin.py -d << EOF
4
8
ihipiz iy icigxpxz
EOF

echo "------ Running vigenere Cipher ------"
echo "CIPHER"
python3 vigenere.py -c << EOF
hola mundo
clave
EOF
echo ""
echo "DECIPHER"
python3 vigenere.py -d << EOF
jzlvdñenys
clave
EOF