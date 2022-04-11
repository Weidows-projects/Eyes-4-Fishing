###
 # @?: *********************************************************************
 # @Author: Weidows
 # @Date: 2022-04-11 15:43:05
 # @LastEditors: Weidows
 # @LastEditTime: 2022-04-11 16:27:24
 # @FilePath: \Blog-private\source\_posts\public-post\notebook\convert.sh
 # @Description:
 # @!: *********************************************************************
###

# 转到 convert path
cd $(dirname $0)

# convert all
jupyter nbconvert --to markdown *.ipynb

# hexo 中图片的引用很诡异, 这么做是为了正常显示
# (需要设置_config.yml中 post_asset_folder: true)
mv ML_files ML/
