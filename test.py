import asyncio
import websockets
import sys
import wave



def main():
    """TODO change following code to the example presented in folowing video (real time txt output using vosk)
    https://www.youtube.com/watch?v=SqVeAxrPAB0
    """
    print("Hello Affen")

    async def run_test(uri):
        async with websockets.connect(uri) as websocket:

            wf = wave.open(sys.argv[1], "rb")
            await websocket.send('{ "config" : { "sample_rate" : %d } }' % (wf.getframerate()))
            buffer_size = int(wf.getframerate() * 0.2) # 0.2 seconds of audio
            while True:
                data = wf.readframes(buffer_size)

                if len(data) == 0:
                    break

                await websocket.send(data)
                print (await websocket.recv())

            await websocket.send('{"eof" : 1}')
            print (await websocket.recv())

    asyncio.run(run_test('ws://localhost:2700'))

if __name__ == '__main__':
    main()