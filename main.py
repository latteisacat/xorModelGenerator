import onnx.checker
import torch.onnx
import torch.nn as nn
import torch

# 주어진 가중치
weights = {
    'w1': torch.tensor([[3.4243], [3.4299]], dtype=torch.float32),
    'b1': torch.tensor([-5.3119], dtype=torch.float32),
    'w2': torch.tensor([[4.4863], [4.4830]], dtype=torch.float32),
    'b2': torch.tensor([-1.7982], dtype=torch.float32),
    'w3': torch.tensor([[-7.1722], [6.7997]], dtype=torch.float32),
    'b3': torch.tensor([-3.0611], dtype=torch.float32),
}


# 사용자 정의 모델 클래스
class CustomModel(nn.Module):
    def __init__(self, weights):
        super(CustomModel, self).__init__()
        self.weights = weights

    def forward(self, x):
        f1 = torch.sigmoid(torch.matmul(x, self.weights['w1']) + self.weights['b1'])
        f2 = torch.sigmoid(torch.matmul(x, self.weights['w2']) + self.weights['b2'])
        output = torch.sigmoid(torch.matmul(torch.cat((f1, f2), 1), self.weights['w3']) + self.weights['b3'])
        return output


# 모델 인스턴스 생성
model = CustomModel(weights)

# 모델을 추론 모드로 설정
model.eval()

# 입력 데이터
input_data = torch.tensor([[0.45, 0.45]], dtype=torch.float32)

print(input_data)
result = model.forward(input_data)
print(result)
# 모델을 ONNX로 변환
torch.onnx.export(model, input_data, 'xor_model.onnx', verbose=False)
# onnx_model = onnx.load('./xor_model.onnx')
# onnx.checker.check_model(onnx_model)
# print(onnx.helper.printable_graph(onnx_model.graph))
