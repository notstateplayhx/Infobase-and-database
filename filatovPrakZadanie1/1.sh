#!/bin/bash

if [ -z "$1" ]; then
    echo "Ошибка: не передан аргумент с именем файла"
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "Ошибка: исходный файл не существует"
    exit 1
fi

for ((i=1; i<=10; i++)); do
    filename=$(date "+%m-%d")_$i.txt
    cp "$1" "$filename"
    sleep 3
done

echo "Копирование завершено!"
