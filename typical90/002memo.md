## 002 - Encyclopedia of Parentheses (★3)
**bit全探索やitertoolsのproductを使うとすごく楽**
使われる文字は`(` `)`の二文字だけなので、これらを並べる方法は$2^N$通り、今回の制約は$1\leq N\leq20$なので全探索で間に合う
$2^{20}=1048576 \fallingdotseq 10^6$

### 解法メモ
bit全探索を実装しなくても、pythonならitertoolsのproductで直積を取れるので、楽にコーディング可能
[productのドキュメント](https://docs.python.org/3/library/itertools.html#itertools.product)