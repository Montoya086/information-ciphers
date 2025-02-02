echo "------ Running Caesar Cipher ------"
echo "CIPHER"
python3 caesar.py -c << EOF
hello world
EOF
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
echo "DECIPHER"
python3 afin.py -d << EOF
4
8
ihipiz iy icigxpxz
EOF