from flask import Flask, render_template, request
import requests
import json

app = Flask('')

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/details')
def details():
  sneak1 = ['', '', '', '', '', '', '', '', '', '', '']
  searchdata = request.args.get('id')
  url = requests.get(f'https://sneak.jacebillingsley.repl.co/search2/{searchdata}')
  text = url.text
  try:
    data = json.loads(text)
  except:
    return render_template('error.html')
  try:
    sneak1[0] = data["brand"]
    sneak1[1] = data["shoeName"]
    sneak1[2] = data["colorway"]
    sneak1[3] = data["styleID"]
    sneak1[10] = data["thumbnail"]
  except:
    return render_template('error.html')
  try:
    sneak1[5] = data["lowestResellPrice"]["goat"]
    sneak1[8] = data["resellLinks"]["goat"]
  except:
    sneak1[5] = 'Unable to Fetch Data'
    sneak1[8] = 'Unable to Fetch Data'
  try:
    sneak1[6] = data["lowestResellPrice"]["flightClub"]
    sneak1[9] = data["resellLinks"]["flightClub"]
  except:
    sneak1[6] = 'Unable to Fetch Data'
    sneak1[9] = 'Unable to Fetch Data'
  try:
    sneak1[4] = data["lowestResellPrice"]["stockX"]
    sneak1[7] = data["resellLinks"]["stockX"]
  except:
    sneak1[7] = 'Unable to Fetch Data'
    sneak1[4] = 'Unable to Fetch Data'
  return render_template('detail.html', sneak1 = sneak1)

@app.route('/search')
def number2():
  nextpage = '2'
  page='1'
  totalpages = '5'

  prevenable = 'disabled'
  sneak1 = ['', '', 'hidden', '', '', '']
  sneak2 = ['', '', 'hidden', '', '', '']
  sneak3 = ['', '', 'hidden', '', '', '']
  sneak4 = ['', '', 'hidden', '', '', '']
  sneak5 = ['', '', 'hidden', '', '', '']
  sneak6 = ['', '', 'hidden', '', '', '']
  sneak7 = ['', '', 'hidden', '', '', '']
  sneak8 = ['', '', 'hidden', '', '', '']
  sneak9 = ['', '', 'hidden', '', '', '']
  sneak10 = ['', '', 'hidden', '', '', '']
  searchdata = request.args.get('searchdata')
  url = requests.get(f'https://sneak.jacebillingsley.repl.co/search/{searchdata}')
  text = url.text
  try:
    data = json.loads(text)
  except:
    return render_template('index.html')
  if searchdata == None:
    searchdata = "Popular"
  try:
    sneak1[0] = data[0]["thumbnail"]
    sneak1[1] = data[0]["shoeName"]
    sneak1[2] = "visible"
    sneak1[3] = data[0]["shoeName"]
    sneak1[4] = data[0]["lowestResellPrice"]["goat"]
    sneak1[5] = data[0]["styleID"]
  except:
    pass
  try:
    sneak2[0] = data[1]["thumbnail"]
    sneak2[1] = data[1]["shoeName"]
    sneak2[2] = "visible"
    sneak2[3] = data[1]["shoeName"]
    sneak2[4] = data[1]["lowestResellPrice"]["goat"]
    sneak2[5] = data[1]["styleID"]
  except:
    pass
  try:
    sneak3[0] = data[2]["thumbnail"]
    sneak3[1] = data[2]["shoeName"]
    sneak3[2] = "visible"
    sneak3[3] = data[2]["shoeName"]
    sneak3[4] = data[2]["lowestResellPrice"]["goat"]
    sneak3[5] = data[2]["styleID"]
  except:
    pass
  try:
    sneak4[0] = data[3]["thumbnail"]
    sneak4[1] = data[3]["shoeName"]
    sneak4[2] = "visible"
    sneak4[3] = data[3]["shoeName"]
    sneak4[4] = data[3]["lowestResellPrice"]["goat"]
    sneak4[5] = data[3]["styleID"]
  except:
    pass
  try:
    sneak5[0] = data[4]["thumbnail"]
    sneak5[1] = data[4]["shoeName"]
    sneak5[2] = "visible"
    sneak5[3] = data[4]["shoeName"]
    sneak5[4] = data[4]["lowestResellPrice"]["goat"]
    sneak5[5] = data[4]["styleID"]
  except:
    pass
  try:
    sneak6[0] = data[5]["thumbnail"]
    sneak6[1] = data[5]["shoeName"]
    sneak6[2] = "visible"
    sneak6[3] = data[5]["shoeName"]
    sneak6[4] = data[5]["lowestResellPrice"]["goat"]
    sneak6[5] = data[5]["styleID"]
  except:
    pass
  try:
    sneak7[0] = data[6]["thumbnail"]
    sneak7[1] = data[6]["shoeName"]
    sneak7[2] = "visible"
    sneak7[3] = data[6]["shoeName"]
    sneak7[4] = data[6]["lowestResellPrice"]["goat"]
    sneak7[5] = data[6]["styleID"]
  except:
    pass
  try:
    sneak8[0] = data[7]["thumbnail"]
    sneak8[1] = data[7]["shoeName"]
    sneak8[2] = "visible"
    sneak8[3] = data[7]["shoeName"]
    sneak8[4] = data[7]["lowestResellPrice"]["goat"]
    sneak8[5] = data[7]["styleID"]
  except:
    pass
  try:
    sneak9[0] = data[8]["thumbnail"]
    sneak9[1] = data[8]["shoeName"]
    sneak9[2] = "visible"
    sneak9[3] = data[8]["shoeName"]
    sneak9[4] = data[8]["lowestResellPrice"]["goat"]
    sneak9[5] = data[8]["styleID"]
  except:
    pass
  try:
    sneak10[0] = data[9]["thumbnail"]
    sneak10[1] = data[9]["shoeName"]
    sneak10[2] = "visible"
    sneak10[3] = data[9]["shoeName"]
    sneak10[4] = data[9]["lowestResellPrice"]["goat"]
    sneak10[5] = data[9]["styleID"]
  except:
    pass
  return render_template('search.html', **locals())

@app.route('/search2')
def number3():
  page='2'
  nextpage = '3'
  prevpage = ''
  totalpages = '5'

  nextenable = ''
  prevenable = ''
  sneak1 = ['', '', 'hidden', '', '', '']
  sneak2 = ['', '', 'hidden', '', '', '']
  sneak3 = ['', '', 'hidden', '', '', '']
  sneak4 = ['', '', 'hidden', '', '', '']
  sneak5 = ['', '', 'hidden', '', '', '']
  sneak6 = ['', '', 'hidden', '', '', '']
  sneak7 = ['', '', 'hidden', '', '', '']
  sneak8 = ['', '', 'hidden', '', '', '']
  sneak9 = ['', '', 'hidden', '', '', '']
  sneak10 = ['', '', 'hidden', '', '', '']
  searchdata = request.args.get('searchdata')
  url = requests.get(f'https://sneak.jacebillingsley.repl.co/searchamount/20/{searchdata}')
  text = url.text
  try:
    data = json.loads(text)
  except:
    return render_template('index.html')
  if searchdata == None:
    searchdata = "Popular"
  try:
    sneak1[0] = data[10]["thumbnail"]
    sneak1[1] = data[10]["shoeName"]
    sneak1[2] = "visible"
    sneak1[3] = data[10]["shoeName"]
    sneak1[4] = data[10]["lowestResellPrice"]["goat"]
    sneak1[5] = data[10]["styleID"]
  except:
    pass
  try:
    sneak2[0] = data[11]["thumbnail"]
    sneak2[1] = data[11]["shoeName"]
    sneak2[2] = "visible"
    sneak2[3] = data[11]["shoeName"]
    sneak2[4] = data[11]["lowestResellPrice"]["goat"]
    sneak2[5] = data[11]["styleID"]
  except:
    pass
  try:
    sneak3[0] = data[12]["thumbnail"]
    sneak3[1] = data[12]["shoeName"]
    sneak3[2] = "visible"
    sneak3[3] = data[12]["shoeName"]
    sneak3[4] = data[12]["lowestResellPrice"]["goat"]
    sneak3[5] = data[12]["styleID"]
  except:
    pass
  try:
    sneak4[0] = data[13]["thumbnail"]
    sneak4[1] = data[13]["shoeName"]
    sneak4[2] = "visible"
    sneak4[3] = data[13]["shoeName"]
    sneak4[4] = data[13]["lowestResellPrice"]["goat"]
    sneak4[5] = data[13]["styleID"]
  except:
    pass
  try:
    sneak5[0] = data[14]["thumbnail"]
    sneak5[1] = data[14]["shoeName"]
    sneak5[2] = "visible"
    sneak5[3] = data[14]["shoeName"]
    sneak5[4] = data[14]["lowestResellPrice"]["goat"]
    sneak5[5] = data[14]["styleID"]
  except:
    pass
  try:
    sneak6[0] = data[15]["thumbnail"]
    sneak6[1] = data[15]["shoeName"]
    sneak6[2] = "visible"
    sneak6[3] = data[15]["shoeName"]
    sneak6[4] = data[15]["lowestResellPrice"]["goat"]
    sneak6[5] = data[15]["styleID"]
  except:
    pass
  try:
    sneak7[0] = data[16]["thumbnail"]
    sneak7[1] = data[16]["shoeName"]
    sneak7[2] = "visible"
    sneak7[3] = data[16]["shoeName"]
    sneak7[4] = data[16]["lowestResellPrice"]["goat"]
    sneak7[5] = data[16]["styleID"]
  except:
    pass
  try:
    sneak8[0] = data[17]["thumbnail"]
    sneak8[1] = data[17]["shoeName"]
    sneak8[2] = "visible"
    sneak8[3] = data[17]["shoeName"]
    sneak8[4] = data[17]["lowestResellPrice"]["goat"]
    sneak8[5] = data[17]["styleID"]
  except:
    pass
  try:
    sneak9[0] = data[18]["thumbnail"]
    sneak9[1] = data[18]["shoeName"]
    sneak9[2] = "visible"
    sneak9[3] = data[18]["shoeName"]
    sneak9[4] = data[18]["lowestResellPrice"]["goat"]
    sneak9[5] = data[18]["styleID"]
  except:
    pass
  try:
    sneak10[0] = data[19]["thumbnail"]
    sneak10[1] = data[19]["shoeName"]
    sneak10[2] = "visible"
    sneak10[3] = data[19]["shoeName"]
    sneak10[4] = data[19]["lowestResellPrice"]["goat"]
    sneak10[5] = data[19]["styleID"]
  except:
    pass
  return render_template('search.html', **locals())

@app.route('/search3')
def number4():
  page='3'
  nextpage='4'
  totalpages = '5'
  nextenable = ''
  prevpage='2'
  sneak1 = ['', '', 'hidden', '', '', '']
  sneak2 = ['', '', 'hidden', '', '', '']
  sneak3 = ['', '', 'hidden', '', '', '']
  sneak4 = ['', '', 'hidden', '', '', '']
  sneak5 = ['', '', 'hidden', '', '', '']
  sneak6 = ['', '', 'hidden', '', '', '']
  sneak7 = ['', '', 'hidden', '', '', '']
  sneak8 = ['', '', 'hidden', '', '', '']
  sneak9 = ['', '', 'hidden', '', '', '']
  sneak10 = ['', '', 'hidden', '', '', '']
  searchdata = request.args.get('searchdata')
  url = requests.get(f'https://sneak.jacebillingsley.repl.co/searchamount/30/{searchdata}')
  text = url.text
  try:
    data = json.loads(text)
  except:
    return render_template('index.html')
  if searchdata == None:
    searchdata = "Popular"
  try:
    sneak1[0] = data[20]["thumbnail"]
    sneak1[1] = data[20]["shoeName"]
    sneak1[2] = "visible"
    sneak1[3] = data[20]["shoeName"]
    sneak1[4] = data[20]["lowestResellPrice"]["goat"]
    sneak1[5] = data[20]["styleID"]
  except:
    pass
  try:
    sneak2[0] = data[21]["thumbnail"]
    sneak2[1] = data[21]["shoeName"]
    sneak2[2] = "visible"
    sneak2[3] = data[21]["shoeName"]
    sneak2[4] = data[21]["lowestResellPrice"]["goat"]
    sneak2[5] = data[21]["styleID"]
  except:
    pass
  try:
    sneak3[0] = data[22]["thumbnail"]
    sneak3[1] = data[22]["shoeName"]
    sneak3[2] = "visible"
    sneak3[3] = data[22]["shoeName"]
    sneak3[4] = data[22]["lowestResellPrice"]["goat"]
    sneak3[5] = data[22]["styleID"]
  except:
    pass
  try:
    sneak4[0] = data[23]["thumbnail"]
    sneak4[1] = data[23]["shoeName"]
    sneak4[2] = "visible"
    sneak4[3] = data[23]["shoeName"]
    sneak4[4] = data[23]["lowestResellPrice"]["goat"]
    sneak4[5] = data[23]["styleID"]
  except:
    pass
  try:
    sneak5[0] = data[24]["thumbnail"]
    sneak5[1] = data[24]["shoeName"]
    sneak5[2] = "visible"
    sneak5[3] = data[24]["shoeName"]
    sneak5[4] = data[24]["lowestResellPrice"]["goat"]
    sneak5[5] = data[24]["styleID"]
  except:
    pass
  try:
    sneak6[0] = data[25]["thumbnail"]
    sneak6[1] = data[25]["shoeName"]
    sneak6[2] = "visible"
    sneak6[3] = data[25]["shoeName"]
    sneak6[4] = data[25]["lowestResellPrice"]["goat"]
    sneak6[5] = data[25]["styleID"]
  except:
    pass
  try:
    sneak7[0] = data[26]["thumbnail"]
    sneak7[1] = data[26]["shoeName"]
    sneak7[2] = "visible"
    sneak7[3] = data[26]["shoeName"]
    sneak7[4] = data[26]["lowestResellPrice"]["goat"]
    sneak7[5] = data[26]["styleID"]
  except:
    pass
  try:
    sneak8[0] = data[27]["thumbnail"]
    sneak8[1] = data[27]["shoeName"]
    sneak8[2] = "visible"
    sneak8[3] = data[27]["shoeName"]
    sneak8[4] = data[27]["lowestResellPrice"]["goat"]
    sneak8[5] = data[27]["styleID"]
  except:
    pass
  try:
    sneak9[0] = data[28]["thumbnail"]
    sneak9[1] = data[28]["shoeName"]
    sneak9[2] = "visible"
    sneak9[3] = data[28]["shoeName"]
    sneak9[4] = data[28]["lowestResellPrice"]["goat"]
    sneak9[5] = data[28]["styleID"]
  except:
    pass
  try:
    sneak10[0] = data[29]["thumbnail"]
    sneak10[1] = data[29]["shoeName"]
    sneak10[2] = "visible"
    sneak10[3] = data[29]["shoeName"]
    sneak10[4] = data[29]["lowestResellPrice"]["goat"]
    sneak10[5] = data[29]["styleID"]
  except:
    pass
  return render_template('search.html', **locals())

@app.route('/search4')
def number5():
  page='4'
  nextpage='5'
  totalpages = '5'
  nextenable = ''
  prevpage='3'
  sneak1 = ['', '', 'hidden', '', '', '']
  sneak2 = ['', '', 'hidden', '', '', '']
  sneak3 = ['', '', 'hidden', '', '', '']
  sneak4 = ['', '', 'hidden', '', '', '']
  sneak5 = ['', '', 'hidden', '', '', '']
  sneak6 = ['', '', 'hidden', '', '', '']
  sneak7 = ['', '', 'hidden', '', '', '']
  sneak8 = ['', '', 'hidden', '', '', '']
  sneak9 = ['', '', 'hidden', '', '', '']
  sneak10 = ['', '', 'hidden', '', '', '']
  searchdata = request.args.get('searchdata')
  url = requests.get(f'https://sneak.jacebillingsley.repl.co/searchamount/40/{searchdata}')
  text = url.text
  try:
    data = json.loads(text)
  except:
    return render_template('index.html')
  if searchdata == None:
    searchdata = "Popular"
  try:
    sneak1[0] = data[30]["thumbnail"]
    sneak1[1] = data[30]["shoeName"]
    sneak1[2] = "visible"
    sneak1[3] = data[30]["shoeName"]
    sneak1[4] = data[30]["lowestResellPrice"]["goat"]
    sneak1[5] = data[30]["styleID"]
  except:
    pass
  try:
    sneak2[0] = data[31]["thumbnail"]
    sneak2[1] = data[31]["shoeName"]
    sneak2[2] = "visible"
    sneak2[3] = data[31]["shoeName"]
    sneak2[4] = data[31]["lowestResellPrice"]["goat"]
    sneak2[5] = data[31]["styleID"]
  except:
    pass
  try:
    sneak3[0] = data[32]["thumbnail"]
    sneak3[1] = data[32]["shoeName"]
    sneak3[2] = "visible"
    sneak3[3] = data[32]["shoeName"]
    sneak3[4] = data[32]["lowestResellPrice"]["goat"]
    sneak3[5] = data[32]["styleID"]
  except:
    pass
  try:
    sneak4[0] = data[33]["thumbnail"]
    sneak4[1] = data[33]["shoeName"]
    sneak4[2] = "visible"
    sneak4[3] = data[33]["shoeName"]
    sneak4[4] = data[33]["lowestResellPrice"]["goat"]
    sneak4[5] = data[33]["styleID"]
  except:
    pass
  try:
    sneak5[0] = data[34]["thumbnail"]
    sneak5[1] = data[34]["shoeName"]
    sneak5[2] = "visible"
    sneak5[3] = data[34]["shoeName"]
    sneak5[4] = data[34]["lowestResellPrice"]["goat"]
    sneak5[5] = data[34]["styleID"]
  except:
    pass
  try:
    sneak6[0] = data[35]["thumbnail"]
    sneak6[1] = data[35]["shoeName"]
    sneak6[2] = "visible"
    sneak6[3] = data[35]["shoeName"]
    sneak6[4] = data[35]["lowestResellPrice"]["goat"]
    sneak6[5] = data[35]["styleID"]
  except:
    pass
  try:
    sneak7[0] = data[36]["thumbnail"]
    sneak7[1] = data[36]["shoeName"]
    sneak7[2] = "visible"
    sneak7[3] = data[36]["shoeName"]
    sneak7[4] = data[36]["lowestResellPrice"]["goat"]
    sneak7[5] = data[36]["styleID"]
  except:
    pass
  try:
    sneak8[0] = data[37]["thumbnail"]
    sneak8[1] = data[37]["shoeName"]
    sneak8[2] = "visible"
    sneak8[3] = data[37]["shoeName"]
    sneak8[4] = data[37]["lowestResellPrice"]["goat"]
    sneak8[5] = data[37]["styleID"]
  except:
    pass
  try:
    sneak9[0] = data[38]["thumbnail"]
    sneak9[1] = data[38]["shoeName"]
    sneak9[2] = "visible"
    sneak9[3] = data[38]["shoeName"]
    sneak9[4] = data[38]["lowestResellPrice"]["goat"]
    sneak9[5] = data[38]["styleID"]
  except:
    pass
  try:
    sneak10[0] = data[39]["thumbnail"]
    sneak10[1] = data[39]["shoeName"]
    sneak10[2] = "visible"
    sneak10[3] = data[39]["shoeName"]
    sneak10[4] = data[39]["lowestResellPrice"]["goat"]
    sneak10[5] = data[39]["styleID"]
  except:
    pass
  return render_template('search.html', **locals())

@app.route('/search5')
def number6():
  page='5'
  nextpage='5'
  totalpages = '5'
  nextenable = 'disabled'
  prevpage='4'
  sneak1 = ['', '', 'hidden', '', '', '']
  sneak2 = ['', '', 'hidden', '', '', '']
  sneak3 = ['', '', 'hidden', '', '', '']
  sneak4 = ['', '', 'hidden', '', '', '']
  sneak5 = ['', '', 'hidden', '', '', '']
  sneak6 = ['', '', 'hidden', '', '', '']
  sneak7 = ['', '', 'hidden', '', '', '']
  sneak8 = ['', '', 'hidden', '', '', '']
  sneak9 = ['', '', 'hidden', '', '', '']
  sneak10 = ['', '', 'hidden', '', '', '']
  searchdata = request.args.get('searchdata')
  url = requests.get(f'https://sneak.jacebillingsley.repl.co/searchamount/50/{searchdata}')
  text = url.text
  try:
    data = json.loads(text)
  except:
    return render_template('index.html')
  if searchdata == None:
    searchdata = "Popular"
  try:
    sneak1[0] = data[40]["thumbnail"]
    sneak1[1] = data[40]["shoeName"]
    sneak1[2] = "visible"
    sneak1[3] = data[40]["shoeName"]
    sneak1[4] = data[40]["lowestResellPrice"]["goat"]
    sneak1[5] = data[40]["styleID"]
  except:
    pass
  try:
    sneak2[0] = data[41]["thumbnail"]
    sneak2[1] = data[41]["shoeName"]
    sneak2[2] = "visible"
    sneak2[3] = data[41]["shoeName"]
    sneak2[4] = data[41]["lowestResellPrice"]["goat"]
    sneak2[5] = data[41]["styleID"]
  except:
    pass
  try:
    sneak3[0] = data[42]["thumbnail"]
    sneak3[1] = data[42]["shoeName"]
    sneak3[2] = "visible"
    sneak3[3] = data[42]["shoeName"]
    sneak3[4] = data[42]["lowestResellPrice"]["goat"]
    sneak3[5] = data[42]["styleID"]
  except:
    pass
  try:
    sneak4[0] = data[43]["thumbnail"]
    sneak4[1] = data[43]["shoeName"]
    sneak4[2] = "visible"
    sneak4[3] = data[43]["shoeName"]
    sneak4[4] = data[43]["lowestResellPrice"]["goat"]
    sneak4[5] = data[43]["styleID"]
  except:
    pass
  try:
    sneak5[0] = data[44]["thumbnail"]
    sneak5[1] = data[44]["shoeName"]
    sneak5[2] = "visible"
    sneak5[3] = data[44]["shoeName"]
    sneak5[4] = data[44]["lowestResellPrice"]["goat"]
    sneak5[5] = data[44]["styleID"]
  except:
    pass
  try:
    sneak6[0] = data[45]["thumbnail"]
    sneak6[1] = data[45]["shoeName"]
    sneak6[2] = "visible"
    sneak6[3] = data[45]["shoeName"]
    sneak6[4] = data[45]["lowestResellPrice"]["goat"]
    sneak6[5] = data[45]["styleID"]
  except:
    pass
  try:
    sneak7[0] = data[46]["thumbnail"]
    sneak7[1] = data[46]["shoeName"]
    sneak7[2] = "visible"
    sneak7[3] = data[46]["shoeName"]
    sneak7[4] = data[46]["lowestResellPrice"]["goat"]
    sneak7[5] = data[46]["styleID"]
  except:
    pass
  try:
    sneak8[0] = data[47]["thumbnail"]
    sneak8[1] = data[47]["shoeName"]
    sneak8[2] = "visible"
    sneak8[3] = data[47]["shoeName"]
    sneak8[4] = data[47]["lowestResellPrice"]["goat"]
    sneak8[5] = data[47]["styleID"]
  except:
    pass
  try:
    sneak9[0] = data[48]["thumbnail"]
    sneak9[1] = data[48]["shoeName"]
    sneak9[2] = "visible"
    sneak9[3] = data[48]["shoeName"]
    sneak9[4] = data[48]["lowestResellPrice"]["goat"]
    sneak9[5] = data[48]["styleID"]
  except:
    pass
  try:
    sneak10[0] = data[49]["thumbnail"]
    sneak10[1] = data[49]["shoeName"]
    sneak10[2] = "visible"
    sneak10[3] = data[49]["shoeName"]
    sneak10[4] = data[49]["lowestResellPrice"]["goat"]
    sneak10[5] = data[49]["styleID"]
  except:
    pass
  return render_template('search.html', **locals())

app.run('0.0.0.0')