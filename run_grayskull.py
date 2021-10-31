"""Touch up the conda recipe from grayskull using conda-souschef."""
import os
from os.path import join
from souschef.recipe import Recipe
import chem_wasserstein

os.system(
    "grayskull pypi {0}=={1}".format(
        chem_wasserstein.__name__, chem_wasserstein.__version__
    )
)

fpath = join("chem_wasserstein", "meta.yaml")
fpath2 = join("scratch", "meta.yaml")
my_recipe = Recipe(load_file=fpath)
my_recipe["requirements"]["host"].append("flit")
my_recipe.save(fpath)
my_recipe.save(fpath2)
