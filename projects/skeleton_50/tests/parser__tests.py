from nose.tools import *
from game.game import lexicon
from game.parser import Sentence
import game.parser as gp

def test_sentence():
    lex = lexicon("d")
    word_list = lex.scan('bear kill princess')
    s = gp.parse_sentence(word_list)
    sent = Sentence(('noun', 'bear'),('verb', 'kill'),('noun', 'princess'))
    assert_equal(sent.subject, 'bear')
    assert_equal(sent.verb, 'kill')
    assert_equal(sent.object, 'princess')

def test_peek():
    lex = lexicon("d")
    word_list = lex.scan('princess')
    assert_equal(gp.peek(word_list), 'noun')

def test_match():
    lex = lexicon("d")
    word_list = lex.scan('princess')
    assert_equal(gp.match(word_list, 'noun'), ('noun', 'princess'))
    assert_equal(gp.match(word_list, 'stop'), None)

def test_skip():
    lex = lexicon("d")
    word_list = lex.scan('bear kill princess')
    assert_equal(word_list, [('noun', 'bear'), ('verb', 'kill'), ('noun', 'princess')])
    gp.skip(word_list, 'noun')
    assert_equal(word_list, [('verb', 'kill'), ('noun', 'princess')])

def test_parse_verb():
    lex = lexicon("d")
    word_list = lex.scan('it kill princess')
    assert_equal(gp.parse_verb(word_list), ('verb', 'kill'))
    word_list = lex.scan('bear kill princess')
    assert_raises(gp.ParserError, gp.parse_verb, word_list)

def test_parse_object():
    lex = lexicon("d")
    word_list = lex.scan('of west')
    assert_equal(gp.parse_object(word_list), ('direction', 'west'))
    word_list = lex.scan('from right')
    assert_equal(gp.parse_object(word_list), ('direction', 'right'))
    word_list = lex.scan('at down')
    assert_equal(gp.parse_object(word_list), ('direction', 'down'))
    word_list = lex.scan('the it')
    
    assert_raises(gp.ParserError, gp.parse_object, word_list)

def test_parse_subject():
    lex = lexicon("d")
    word_list = lex.scan('kill princess')
    subj = ('noun', 'bear')
    s = gp.parse_subject(word_list, subj)

def test_parse_sentence():
    lex = lexicon("d")
    word_list = lex.scan('bear kill princess')
    s = gp.parse_sentence(word_list)
    word_list = lex.scan('it kill princess')
    s = gp.parse_sentence(word_list)
    word_list = lex.scan('east open door')
    assert_raises(gp.ParserError, gp.parse_sentence, word_list)

