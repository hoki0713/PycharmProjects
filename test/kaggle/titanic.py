class Entity:
    context: str
    fname: str
    train: object
    test: object
    id: str
    label: str

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> object: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> object: return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, label): self._label = label

# context (str), fname (str), train (object), test (object), id(str), label(str)

class Service:
    def __init__(self):
        self.entity = Entity()

    def new_entity(self, payload):
        this = self.entity
        this.context = './data/'
        this.fname = payload


class Controller:
    def __init__(self):
        # 파이썬에서 Entity(속성)와 Service(기능)이 합쳐지면 객체가 되는데 그걸 Model 이라고 부름.
        self.entity = Entity()
        self.service = Service()

    def modeling(self, train, test):
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def preprocess(self, train, test):
        service = self.service




def print_menu():
    print("메뉴선택\n 0.종료\n 1.시작")
    return input()

app = Controller()

while 1:
    menu = print_menu()
    if menu == 0:
        break
    if menu == 1:
        pass