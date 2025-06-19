FROM alpine:3.20

# Kopijuojame programą į konteinerį
COPY app.sh /app.sh

# Leidžiame vykdyti
RUN chmod +x /app.sh

# Numatytas paleidimo komandą
CMD ["/app.sh"]