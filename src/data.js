function test() {

	let json = '{"result": true, "count": 42}'
	let obj = JSON.parse('data/affixes_test.json')

	console.log(obj.count)
	console.log(obj.result)
}