import mixed as mixed


class _Assert:

    @staticmethod
    def array_of(
            self,
            class_name: str,
            items: list,
    ) -> None:
        for item in items:
            self.of(class_name, item)

    @staticmethod
    def instance_of(
            class_name: str,
            instance: mixed,
    ) -> None:
        if not isinstance(instance, class_name):
            raise TypeError(f'Expected {class_name} but got {type(instance)}')
