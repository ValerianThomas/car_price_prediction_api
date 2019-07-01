from . import config

def validate_inputs (*, data) -> dict:
  data = data.copy()
  """
  print("before", len(data.index))
  # check numercial value nan
  for item in config.NUMERICAL_FEATURES_TO_KEEP:
    if data[item].isna().sum() > 0 :
      mask_number = data[item].isna().sum() == 0
      data = data.loc[mask_number,:]
  # check  and remove index with log value negative
  for item in config.FEATURE_2_LOG:
    mask_log = data[item] >= 0
    data = data.loc[mask_log,:]

  print("after", len(data.index))
  """
  return data