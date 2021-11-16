# protos

### command for bots
```
python -m grpc_tools.protoc -I../protos/candles/ --python_out=./bot_app/grpc_generated --grpc_python_out=./bot_app/grpc_generated ../protos/candles/candle.proto --proto_path=../protos/candles
```
