###
 # @?: *********************************************************************
 # @Author: Weidows
 # @Date: 2022-04-11 15:43:05
 # @LastEditors: Weidows
 # @LastEditTime: 2022-07-01 19:54:04
 # @FilePath: \Blog-private\source\_posts\public-post\notebook\convert.sh
 # @Description:
 # @!: *********************************************************************
###

# 转到 convert path
cd $(dirname $0)

# convert list
paths=(
  # .
  # .
  # .
  .
  # ../../python
)

name=(
  # DL
  # ML
  # MM-Detection
  伪随机数发生器
  # 杂
)

dist=(
  # ../../python/code
  # ../../python/code
  # ../../python/code
  ../../python/code
  # ../../python
)

for i in "${!paths[@]}"; do
  rm -rf ${dist[$i]}/${name[$i]}/${name[$i]}_files

  jupyter nbconvert \
    --to markdown ${paths[$i]}/${name[$i]}/*.ipynb \
    --output ${name[$i]}

  # 处理输出中的特殊字符 (XML不支持会报错)
  sed -i "s///g" ${paths[$i]}/${name[$i]}/${name[$i]}.md

  # hexo 中图片的引用很诡异, 这么做是为了正常显示
  # (需要设置_config.yml中 post_asset_folder: true)
  mv ${paths[$i]}/${name[$i]}/${name[$i]}.md ${dist[$i]}
  mkdir ${dist[$i]}/${name[$i]}
  mv ${paths[$i]}/${name[$i]}/${name[$i]}_files ${dist[$i]}/${name[$i]}
done
