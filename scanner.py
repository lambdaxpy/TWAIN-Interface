"""
module scanner.py

This module provides all functionalities dealing with TWAIN-compatible Scanners.
"""
import os
from enum_types import DriverArchitecture
from exceptions import WrongArchitectureException
from constants import TWAIN_32_BIT_PATH, TWAIN_64_BIT_PATH

class Scanner():
    def __init__(self, name: str):
        """
        __init__ Constructor

        Overloading standard constructor.

        :param name: scanner name
        :type name: str
        """
        self._name = name

    def __init__(self):
        """
        __init__ Constructor

        If name is unknown.
        """
        None


class ScannerList():
    """
    ScannerList class

    This class implements the functionality of having an overview of all available 
    TWAIN-Scanners.
    """
    @staticmethod
    def list_available_scanners() -> list:
        """
        list_available_scanners function

        returns all available scanners, wheter
        running on 32-bit or 64-bit drivers.
        """
        return ScannerList.list_available_scanners_of_arch(DriverArchitecture.BIT_32).extend(
            ScannerList.list_available_scanners_of_arch(DriverArchitecture.BIT_64))

    @staticmethod
    def list_available_scanners_of_arch(bit: DriverArchitecture) -> list:
        """
        list_available_scanners function

        returns all available scanners, running on a given
        driver architecture (32-bit, 64-bit).
        """
        if bit == DriverArchitecture.BIT_32:
            return ScannerList._get_drivers_from_folder(TWAIN_32_BIT_PATH)
        elif bit == DriverArchitecture.BIT_64:
            return ScannerList._get_drivers_from_folder(TWAIN_64_BIT_PATH)
        else:
            raise WrongArchitectureException("You have chosen the wrong architecture! Choose wheter 32-bit or 64-bit -> DriverArchitecture Enum")


    @staticmethod
    def _get_drivers_from_folder(path: str) -> list:
        """
        _get_driver_from_folder function

        returns a list of founded drivers
        within a folder.

        :param path: folder path
        :type path: str
        :return: a list of names
        :rtype: list
        """
        return [file_path for file_path in os.listdir(os.path.abspath(path)) if os.path.isfile(os.path.abspath(file_path))]

    @staticmethod
    def check_scanner_available(name: str):
        """
        check_scanner_available function

        checks, wheter a given scanner exists or not.

        :param name: scanner name
        :type name: str
        """

if __name__ == "__main__":
    print(ScannerList.list_available_scanners())

