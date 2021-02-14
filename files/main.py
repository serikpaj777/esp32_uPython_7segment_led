from machine import Pin
from time import sleep

# common anode
led_on = 0
led_off = 1
# common cathode
# led_on = 1
# led_off = 0

led_a = Pin(15, Pin.OUT)
led_b = Pin(2, Pin.OUT)
led_c = Pin(4, Pin.OUT)
led_d = Pin(21, Pin.OUT)
led_e = Pin(19, Pin.OUT)
led_f = Pin(18, Pin.OUT)
led_g = Pin(5, Pin.OUT)

#      led
#      a
#   f     b
#      g
#   e     c
#      d
led = [led_a, led_b, led_c, led_d, led_e, led_f, led_g]

# ledFULL  "0"
#          "1"
#          "2"
#          "3"
#          "4"
#          "5"
#          "6"
#          "7"
#          "8"
#          "9"
ledFULL = [[led_a, led_b, led_c, led_d, led_e, led_f],
           [led_b, led_c],
           [led_a, led_b, led_d, led_e, led_g],
           [led_a, led_b, led_c, led_d, led_g],
           [led_b, led_c, led_f, led_g],
           [led_a, led_c, led_d, led_f, led_g],
           [led_a, led_c, led_d, led_e, led_f, led_g],
           [led_a, led_b, led_c],
           [led_a, led_b, led_c, led_d, led_e, led_f, led_g],
           [led_a, led_b, led_c, led_d, led_f, led_g]]

for i in led:
    i.value(led_off)
sleep(0.3)

def web_page():
    html = """
<html>
    <head>
        <title>my ESP32 Access Point</title>
        <style>
            .b_on_off{
                background-color: #FF4500; /* OrangeRed */
                border: none;
                border-radius: 4px;
                color: white;
                padding: 0px 5px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 40px;
                margin: 5px 5px;}
            
            .button {
                background-color: #4CAF50; /* Green */
                border: none;
                border-radius: 4px;
                color: white;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 8px;
                position: relative;}
            
            .button_v{
                padding: 40px 10px;}
            
            .button_h{
                padding: 7px 50px;}

            .b_a{}
            .b_bc{left: +50px;}
            .b_fe{left: -50px;}
            .b_g{}
            
        </style>
    </head>
    
    <body>
    <center>
        <h1>ESP32 Access Point '7seg. LED'</h1>
        <a href="/?l=on"><button class="b_on_off">all on</button></a>
        <a href="/?l=off"><button class="b_on_off">all off</button></a>
        <p></p>
    </center>
    <center>
        <div>
        <a href="/?l=a"><button class="button button_h b_a">a</button>
        </a><p></p>
        </div>
        <div>
        <a href="/?l=f"><button class="button button_v b_fe">f</button></a>
        <a href="/?l=b"><button class="button button_v b_bc">b</button></a>
        <p></p>
        </div>
        <div>
        <a href="/?l=g"><button class="button button_h b_g">g</button></a>
        <p></p>
        </div>
        <div>
        <a href="/?l=e"><button class="button button_v b_fe">e</button></a>
        <a href="/?l=c"><button class="button button_v b_bc">c</button></a>
        <p></p>
        </div>
        <div>
        <a href="/?l=d"><button class="button button_h b_d">d</button></a>
        </div>
    </center>
        
    </body>
</html>
"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    
    l_a = request.find('/?l=a')
    l_b = request.find('/?l=b')
    l_c = request.find('/?l=c')
    l_d = request.find('/?l=d')
    l_e = request.find('/?l=e')
    l_f = request.find('/?l=f')
    l_g = request.find('/?l=g')
    
    l_off = request.find('/?l=off')
    l_on = request.find('/?l=on')
    
    if l_off == 6:
        for i in led:
            i.value(led_off)

    if l_on == 6:
        for i in led:
            i.value(led_on)

    if l_a == 6:
        if led_a.value() == led_off:
            led_a.value(led_on)
        else:
            led_a.value(led_off)
        
    if l_b == 6:
        if led_b.value() == led_off:
            led_b.value(led_on)
        else:
            led_b.value(led_off)

    if l_c == 6:
        if led_c.value() == led_off:
            led_c.value(led_on)
        else:
            led_c.value(led_off)
        
    if l_d == 6:
        if led_d.value() == led_off:
            led_d.value(led_on)
        else:
            led_d.value(led_off)
        
    if l_e == 6:
        if led_e.value() == led_off:
            led_e.value(led_on)
        else:
            led_e.value(led_off)
        
    if l_f == 6:
        if led_f.value() == led_off:
            led_f.value(led_on)
        else:
            led_f.value(led_off)
        
    if l_g == 6:
        if led_g.value() == led_off:
            led_g.value(led_on)
        else:
            led_g.value(led_off)

    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
