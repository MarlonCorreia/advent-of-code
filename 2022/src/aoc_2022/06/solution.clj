(ns aoc-2022.06.solution)

(def file (slurp "src/aoc_2022/06/input.txt"))

(defn grab-idx [m i]
  (map #(get m %) i))

(defn find-idx [k l]
  (loop [i 1]
    (let [n (grab-idx l (range i (+ i k)))]
      (if (= (count (set n)) k)
        (+ i k)
        (recur (inc i))))))

(defn part-1 []
  (->> file
       (find-idx 4)))

(defn part-2 []
  (->> file
       (find-idx 14)))

(comment
  (part-1)
  (part-2))