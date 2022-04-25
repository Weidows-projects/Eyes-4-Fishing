###
 # @?: *********************************************************************
 # @Author: Weidows
 # @Date: 2022-04-11 15:43:05
 # @LastEditors: Weidows
 # @LastEditTime: 2022-04-25 01:52:18
 # @FilePath: \Blog-private\source\_posts\public-post\notebook\convert.sh
 # @Description:
 # @!: *********************************************************************
###

# 转到 convert path
cd $(dirname $0)

# convert list
paths=(
.
# .
../../python
)

name=(
ML
# DL
杂
)

for i in "${!paths[@]}"; do
  rm -rf ${paths[$i]}/${name[$i]}/${name[$i]}_files

  jupyter nbconvert --to markdown ${paths[$i]}/${name[$i]}/*.ipynb --output ${name[$i]}

  # hexo 中图片的引用很诡异, 这么做是为了正常显示
  # (需要设置_config.yml中 post_asset_folder: true)
  mv ${paths[$i]}/${name[$i]}/*.md ${paths[$i]}
done
