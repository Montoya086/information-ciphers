echo "------ Running Caesar Cipher ------"
echo "CIPHER"
python3 caesar.py -c << EOF
helloworld
EOF
echo ""
echo "DECIPHER"
python3 caesar.py -d << EOF
khññrzruñg
EOF

echo "------ Running afin Cipher ------"
echo "CIPHER"
python3 afin.py -c << EOF
4
8
atacaralamanecer
EOF
echo ""
echo "DECIPHER"
python3 afin.py -d << EOF
4
8
ihipiziyicigxpxz
EOF

echo "------ Running vigenere Cipher ------"
echo "CIPHER"
python3 vigenere.py -c << EOF
holamundo
clave
EOF
echo ""
echo "DECIPHER"
python3 vigenere.py -d << EOF
jzlvpwxdk
clave
EOF