/*For animated background*/

let count = 40;
let c = 1 / count;

function draw() {
	ctx.strokeStyle = 'hsl(180, 70%, 50%)';
	
	ctx.beginPath();
	
	let time_ = Date.now() * 0.0001;
	
	for(let i = 0; i < count; i++) {
		let t_ = i * c;
		
		let time = (time_ + t_) % 1;
		let t = ease.quint.in(time, 0, 1, 1);
		let ty = ease.quint.out(t, 0, 1, 1);
		
		let x = lerp(width, 0, t);
		let y = ty * height * 0.4;
		line(x, y, x, height - y, false);
	}
	
	ctx.stroke();
}