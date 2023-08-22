(ns aoc-2022.05.solution
  (:require [clojure.string :as s]))

(def file (slurp "src/aoc_2022/05/input.txt"))

(defn build-stack [str-stack]
  (let [[head & l] (reverse (s/split-lines str-stack))
        head (filter #(not= \space (second %)) (map-indexed vector head))]
    (->> l
         (map #(map (fn [[idx k]]
                     (hash-map :id k
                               :v (get % idx))) head))
         flatten
         (filter #(not= \space (:v %)))
         (group-by :id)
         (map (fn [[k v]]
                (hash-map (str k) (map #(:v %) v))))
         (into {}))))

(defn apply-move [stack qtd from-k to-k]
  (let [q (-> qtd str parse-long)
        v (take-last q (get stack from-k))
        n (concat (get stack to-k) (reverse v))
        stack (assoc stack from-k (drop-last q (get stack from-k)) to-k n)]
    stack))

(defn apply-moves [moves stack]
  (let [moves (s/split-lines moves)
        m (map #(re-seq #"\d+" %) moves)]
    (loop [[[q f t] & r] m
           s stack]
      (if (empty? r)
        (apply-move s q f t)
        (recur r (apply-move s q f t))))))

(defn part-1 []
  (let [[str-stack moves] (s/split file #"\n\n")
        stack (build-stack str-stack)]
    (->> (apply-moves moves stack)
         sort
         vals
         (map last)
         (apply str))))

(defn apply-move-2 [stack qtd from-k to-k]
  (let [q (-> qtd str parse-long)
        v (take-last q (get stack from-k))
        n (concat (get stack to-k) v)
        stack (assoc stack from-k (drop-last q (get stack from-k)) to-k n)]
    stack))

(defn apply-moves-2 [moves stack]
  (let [moves (s/split-lines moves)
        m (map #(re-seq #"\d+" %) moves)]
    (loop [[[q f t] & r] m
           s stack]
      (if (empty? r)
        (apply-move-2 s q f t)
        (recur r (apply-move-2 s q f t))))))

(defn part-2 []
  (let [[str-stack moves] (s/split file #"\n\n")
        stack (build-stack str-stack)]
    (->> (apply-moves-2 moves stack)
         sort
         vals
         (map last)
         (apply str))))


(comment
  (part-1)
  (part-2)
  )