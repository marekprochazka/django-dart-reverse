String? reverse(String name, [Map? params]) {
    List data = [ {% for url in urls %}{'name':'{{url.name}}', 'url':(Map? params)=>'{{url.path}}', 'num_params':{{url.num_params}}},{% endfor %} ];
    for (var value in data) {
    if (value['name'] == name && value['num_params'] == (params?.length ?? 0))
      return value['url'](params);
  }
  return null;
}




