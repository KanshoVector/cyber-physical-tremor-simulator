# CPS Clinical Data Actuation (ALAMEDA Dataset)

## 概要
パーキンソン病患者の臨床データ（ALAMEDAデータセット）の特定周波数（6.68Hz）を、mBot2を用いて物理空間へ転写するサイバーフィジカルシステム（CPS）。

## 成果物
- [x] Python制御アルゴリズム（位相幾何拘束による制御）
- [x] 非浸透境界条件による安全設計（0° <= θ <= 45°）
- [x] 物理空間への身体的疾患モデル再現

## システム構成
[![システム図のパスをここに記入](images/system_diagram.png)](https://www.notion.so/image/attachment%3Afd0a4b9a-5cd8-4049-907d-0599948a0a7d%3Aimage.png?table=block&id=3644328f-bafc-803b-83c0-e0e196218ac7&spaceId=4251afc8-e3e0-4d83-8abf-920f4c86c591&width=2000&userId=1dbd872b-594c-813c-af5e-00026a72ee71&cache=v2&imgBuildSrc=requestProxiedImageUrl)

## インストール & 実行
mblock

## 技術的ポイント
- 疾患モデルの身体化（情報の身体化）
- 物理的慣性を相殺するパルス制御アルゴリズム
- リアルタイム性の担保

## 参考文献・謝辞
ALAMEDAデータセットの提供元など、参考にした論文やプロジェクトへのリンクを必ず記載してください。
