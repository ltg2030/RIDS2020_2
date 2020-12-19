ls -asl

chmod +x ./afl-showmap
chmod +x ./mutool
for filename in ./crawl_seed/*; do
    ./afl-showmap -q -o "./bitmaps/${filename:13}.bitmap" -m 512 -t 500 ./mutool clean -l -gggg -a -d -z -f -i -s ${filename}
done
